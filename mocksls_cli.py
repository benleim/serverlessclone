import click
import os
import zipfile
    

@click.group()
def cli():
    """A CLI for mocking serverless functionality"""

@cli.command()
@click.option('-f', '--function', required=True, help='The filename for the function to be deployed')
def deploy(function: str):
    """Deploy function to mockserverless"""
    # Zip the function
    zipf = zipfile.ZipFile('zipfile.zip', 'w', zipfile.ZIP_DEFLATED)
    zipf.write(function, arcname=".mocksls")
    zipf.close()
    # Create directory if doesn't exist
    if not os.path.isdir('.mocksls'):
        os.mkdir('.mocksls')
    os.replace('zipfile.zip', '.mocksls/zipfile.zip')
    # Spin up container with zipfile
    

if __name__ == "__main__":
    cli(prog_name="mocksls")