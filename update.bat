aws lambda update-function-code ^
--region eu-central-1 ^
--function-name getJob ^
--zip-file fileb://deployments/OneShiftLambda.zip ^
--profile adminuser ^