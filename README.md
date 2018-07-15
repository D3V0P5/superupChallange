## This is a (very) simple thin solution to the [devops challange](https://github.com/devops-israel/devops-challenge)

Due to security issues credentials are not published.</br>
In order to run ```docker-compose``` you need to create a file named ```.env``` in the same directory of the ```docker-compose.yml```

The content of the file should include :
```bash
AWS_DEFAULT_REGION=<the region>
AWS_ACCESS_KEY_ID=<key>
AWS_SECRET_ACCESS_KEY=<access key>
```
(some) of the keys provided separately
