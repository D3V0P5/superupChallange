

for i in  "us-east-2" "us-east-1" "us-west-1" "us-west-2" "ap-south-1" "ap-northeast-2" "ap-northeast-3" "ap-southeast-1" "ap-southeast-2" "ap-northeast-1" "ca-central-1" "cn-north-1" "cn-northwest-1" "eu-central-1" "eu-west-1" "eu-west-2" "eu-west-3" "sa-east-1"
do
	echo $i
  aws --region $i dynamodb get-item --table-name devops-challenge --key '{"code_name":{"S":"thedoctor"}}'
done