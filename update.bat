"C:\Program Files\7-Zip\7z.exe" a deployments\OneShiftLambda.zip OneShiftLambda.py

aws lambda update-function-code ^
--region eu-central-1 ^
--function-name getJob ^
--zip-file fileb://deployments/OneShiftLambda.zip ^
--profile adminuser ^