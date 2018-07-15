## This is a simple thin solution to the [devops challange](https://github.com/devops-israel/devops-challenge)

> Note: My docker image can be found [here](https://hub.docker.com/r/d3v0p5/superup_devops_ch/)</br>
> or simply pull it `docker pull d3v0p5/superup_devops_ch`



Due to security issues credentials are not published.</br>
In order to run `docker-compose` you need to create a file named `.env` in the same directory of the `docker-compose.yml`

The content of the file should include :
```bash
AWS_DEFAULT_REGION=<the region>
AWS_ACCESS_KEY_ID=<key>
AWS_SECRET_ACCESS_KEY=<access key>
```
(some) of the keys provided (to me) separately

> ##### Note: </br>
>Alternative way is to store credentials and config in your `$HOME/.aws` folder.</br>
>see [Configuration and Credential Files](https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html) for details.



Then run `$ docker-compose up`

Wait for the container to come up and then fire up the curl -

```bash
superupChallange (git)-[master] % curl localhost:5000/health
{ status: healthy, container: https://hub.docker.com/r/d3v0p5/superup_devops_ch/ , project: https://github.com/D3V0P5/superupChallange}

superupChallange (git)-[master] % curl localhost:5000/secret
{secret_code:"SOME SECRET CODE"}

superupChallange (git)-[master] %
```
</br>

##### Further details can b found in the [SUMMARY](docs/SUMMARY.md) file


#### Have fun
