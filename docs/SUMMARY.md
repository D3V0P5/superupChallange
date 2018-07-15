#### Major Time Consumers:

 *  ##### Finding the right region.</br>
    Though I haven't supplied with the region (and was told that it is not a must)</br>
    I had to find it out by myself.</br>
    First I stripped/scarped the list from [Here](https://docs.aws.amazon.com/general/latest/gr/rande.html).</br>
    Then I ran the script
    ```bash
    for i in  "us-east-2" "us-east-1" "us-west-1" "us-west-2" "ap-south-1" "ap-northeast-2" "ap-northeast-3" "ap-southeast-1" "ap-southeast-2" "ap-northeast-1" "ca-central-1" "cn-north-1" "cn-northwest-1" "eu-central-1" "eu-west-1" "eu-west-2" "eu-west-3" "sa-east-1"
    do
    	echo $i
      aws --region $i dynamodb get-item --table-name devops-challenge --key '{"code_name":{"S":"thedoctor"}}'
    done ``` 
   
   and waited for the right one... :trollface:
*  ##### Figuring out how to solve security issues regarding private keys</br>
  One can read the following documentation:</br>
  * Travis: [Travis Encryption keys](https://docs.travis-ci.com/user/encryption-keys/#Usage).
  * Docker: [Pass environment variables to containers](https://docs.docker.com/compose/environment-variables/#set-environment-variables-in-containers)

* ### Documenting
  It's what I'm doing right now.</br>
  Some persons just LOVE spending days making power point presentaions. </br>
  I'm not one of them :rage3:  
