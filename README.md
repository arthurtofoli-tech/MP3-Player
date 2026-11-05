<h1 align="center">$ mp3-player</h1>

<p align="center">
Player de música no terminal, feito em Python com pygame.
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-0d1117?style=for-the-badge&logo=python&logoColor=00FF41" />
<img src="https://img.shields.io/badge/pygame-0d1117?style=for-the-badge&logo=python&logoColor=00FF41" />
<img src="https://img.shields.io/badge/CLI-0d1117?style=for-the-badge&logo=gnubash&logoColor=00FF41" />
</p>

---

### > funcionalidades

- Lista automaticamente os arquivos `.mp3` de uma pasta
- Escolha da música pelo número
- Controles durante a reprodução: pausar, retomar, parar e sair
- Tratamento de erros: pygame não instalado, falha de áudio, pasta ou arquivos ausentes e opções inválidas

### > como rodar

```bash
git clone https://github.com/arthurtofoli-tech/mp3-player.git
cd mp3-player
pip install -r requirements.txt
```

Crie uma pasta chamada `chase-jojo` ao lado do `Main.py` e coloque nela os seus arquivos `.mp3`. Depois:

```bash
python Main.py
```

### > comandos

| Tecla | Ação |
|---|---|
| `número` | Toca a música da lista |
| `P` | Pausa |
| `R` | Retoma |
| `S` | Para a música e volta ao menu |
| `Q` | Encerra a reprodução (no menu, encerra o programa) |

### > exemplo

```
***** MP3 Player *****
Lista de músicas:
1. musica-1.mp3
2. musica-2.mp3

Digite o número da música, 'Q' para encerrar: 1
Tocando: musica-1.mp3
Comando: P
Música pausada. Pressione 'R' para retomar.
```

### > estrutura

```
mp3-player/
├── Main.py            # programa principal
├── requirements.txt   # dependências
└── chase-jojo/        # suas músicas (.mp3), não incluídas no repositório
```

### > tecnologias

`Python` · `pygame` · `os`

<p align="center"><code>$ exit 0</code></p>
