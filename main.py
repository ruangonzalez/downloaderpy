import yt_dlp
from rich.console import Console
import os
import time

def limpar():
    os.system("cls")

console = Console()
limpar()

user = os.getlogin()

def baixar_video(url):

    ydl_opts = {
        'quiet' : True,
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'newline': True,
        'progress:': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except:
            console.print("[bold red]Erro ao baixar o vídeo![/bold red]")
            time.sleep(1)


if __name__ == "__main__":

    ativo = True

    while ativo:
        limpar()
        console.print(f"[bold green]Olá, {user}![/bold green]")
        console.print("[bold green]Bem-vindo ao[/bold green] [bold purple]YT Downloader![/bold purple]")
        console.print("[bold pink]--------------------------------------------[/bold pink]")
        console.print("[bold green]Digite a [bold purple]URL[/bold purple] do vídeo que deseja baixar ou digite [bold red]'sair'[/bold red] para sair do programa.[/bold green]")
        url_video = input("")
        if url_video == "sair":
            console.print(f"[bold red]Até mais {user}[/bold red]")
            exit()
        else:
            try:
                baixar_video(url_video)
                console.print("[bold green]Download concluído com sucesso![/bold green]")
                time.sleep(1)
                continue
            except:
                console.print("[bold red]Erro ao baixar o vídeo![/bold red]")
                console.print("[bold red]Voltando ao início...[/bold red]")
                continue
        