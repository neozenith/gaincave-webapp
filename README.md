# GainCave Webapp

WIP trying to build a serverless API through AWS API Gateway / Lambda and the front end is a statically hosted React App.

TODO:
 - Get a POST Lambda deployed
 - Get a POST lambda saving to Aurora Serverless
 - Secure the API using Cognito
 - Create the React form
 - Deploy the react form
 - Create a Login component
 - Login component should get a session from Cognito
 - Get the react form to "be logged in", eg have an auth token.
 - Get the React form to securely post to the API.

## Backend

Use AWS SAM

```bash
brew tap aws/tap
brew install aws-sam-cli
```

Then:

```bash
sam init --runtime python3.8 --dependency-manager pip --output-dir backend --name api
```

```bash
./tasks.py sam
```

 - https://www.youtube.com/watch?v=MipjLaTp5nA
 - https://www.youtube.com/watch?v=o7OHogUcRmI

## Frontend

```bash
npx create-react-app --template typescript --use-npm frontend
```

Alternatively:

```bash
./tasks.py cra frontend
```

Static hosting on AWS S3 and using CloudFront CDN

 - https://www.youtube.com/watch?v=mls8tiiI3uc
