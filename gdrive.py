import click

from gdrive.utils.files import list_files


@click.group("gdrive")
def cli():
    pass


@cli.command("list-files")
@click.option("--fields", type=str, default=None)
@click.option("--page-size", type=int, default=10)
@click.option("--folder-id", type=str, default=None)
@click.option("--q", type=str, default=None)
def list_files_cli(fields, page_size, folder_id, q):
    for file in list_files(
        fields=fields, page_size=page_size, folder_id=folder_id, q=q
    ):
        print(file)


cli.add_command(list_files_cli)

if __name__ == "__main__":
    cli()
