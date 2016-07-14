aws lambda create-function ^
--region eu-central-1 ^
--function-name getJob ^
--zip-file fileb://deployments/OneShiftLambda.zip ^
--role arn:aws:iam::771350019772:role/service-role/OneShiftLambda ^
--handler OneShiftLambda.get_job ^
--runtime python2.7 ^
--profile adminuser ^
--timeout 10 ^
--memory-size 1024
