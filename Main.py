
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

try:
    import pygame
except ImportError:
    pygame = None


def tocar_musica(pasta, song_name):
    if pygame is None:
        print("Erro: a biblioteca 'pygame' não está instalada.")
        return

    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(os.path.join(pasta, song_name))
        pygame.mixer.music.play()

        print(f"Tocando: {os.path.basename(song_name)}")
        print('Pressione "P" para pausar, "R" para retomar,"S" para parar ou "Q" para sair.')
        print("Digite 'Q' para sair.")
    except pygame.error as erro:
        print(f"Erro ao reproduzir a música: {erro}")
        return

    while True:
        comando = input("Comando: ").strip().upper()

        if comando == "P":
            pygame.mixer.music.pause()
            print("Música pausada. Pressione 'R' para retomar.")

        elif comando == "R":
            pygame.mixer.music.unpause()
            print("Música retomada.")

        elif comando == "S":
            pygame.mixer.music.stop()
            print("Música parada.")
            return

        elif comando == "Q":
            print("Encerrando a reprodução...")
            pygame.mixer.music.stop()
            return

        else:
            print("Comando inválido. Use 'P', 'R', 'S' ou 'Q'.")


def main():
    if pygame is None:
        print("Erro: a biblioteca 'pygame' não está instalada.")
        return

    try:
        pygame.mixer.init()
    except pygame.error:
        print("Falha na inicialização do áudio")
        return

    pasta = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "chase-jojo"
    )

    if not os.path.isdir(pasta):
        print(f"Pasta não encontrada: {pasta}")
        pygame.mixer.quit()
        return

    mp3_files = sorted(
        arquivo for arquivo in os.listdir(pasta)
        if arquivo.lower().endswith(".mp3")
    )

    if not mp3_files:
        print("Nenhum arquivo MP3 encontrado na pasta")
        pygame.mixer.quit()
        return

    while True:
        print("\n***** MP3 Player *****")
        print("Lista de músicas:")

        for index, song in enumerate(mp3_files, start=1):
            print(f"{index}. {song}")

        choice_input = input(
            "\nDigite o número da música, 'Q' para encerrar: "
        ).strip()

        comando = choice_input.upper()

        if comando in {"Q"}:
            print("Encerrando o programa...")
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            return

        if not choice_input.isdigit():
            print("Opção inválida. Digite um número ou 'Q'.")
            continue

        indice = int(choice_input)

        if not 1 <= indice <= len(mp3_files):
            print("Número fora da lista.")
            continue

        tocar_musica(pasta, mp3_files[indice - 1])


if __name__ == "__main__":
    main()