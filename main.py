import yt_dlp
from rich.console import Console
from rich.progress import Progress
import os

def limpar():
    os.system("cls")

console = Console()
limpar()

user = os.getlogin()

def progress_hook(d, task, progress):
    if d['status'] == 'downloading':
        percent = d['downloaded_bytes'] / d['total_bytes'] * 100
        progress.update(task, completed=percent)

def baixar_video(url):

    with Progress() as progress:
        task = progress.add_task("[green]Baixando vídeo...[/green]", total=100)

    ydl_opts = {
        'quiet' : True,
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'progress_hooks': [lambda d: progress_hook(d, task, progress)]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    console.print(f"[bold green]Olá, {user}![/bold green]")
    console.print("[bold green]Bem-vindo ao[/bold green] [bold purple]YT Downloader![/bold purple]")
    console.print("[bold pink]--------------------------------------------[/bold pink]")
    console.print("[bold green]Digite a [bold purple]URL[/bold purple] do vídeo que deseja baixar ou digite [bold red]'sair'[/bold red] para sair do programa.[/bold green]")
    url_video = input("")
    if url_video == "sair":
        exit()
    else:
        try:
            baixar_video(url_video)
            console.print("[bold green]Download concluído com sucesso![/bold green]")
        except:
            console.print("[bold red]Erro ao baixar o vídeo![/bold red]")
        
        


input("Pressione Enter para sair...")