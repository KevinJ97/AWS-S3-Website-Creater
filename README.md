# AWS S3 Website Creator

[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)][mitLink]

## About

AWS S3 Website Creator is a Python script using Boto3 to host a static website using the amazing feature that AWS provides. This process is very easy to do if the user just wants to use the GUI to create it. However, to create the websites programmatically this turned out to be significantly harder. During MLH Prime Southwest Regional 2016, we needed a way to create website dynamically with unique names using AWS. This came to be the AWS S3 Website Creator.

## Functionality
- Create AWS Websites with specific bucket names
- Upload any to all files to the S3 Bucket
- Set bucket policies
- Set each file to have unique policies

## Installation

To get started following the instructions:
- Install boto 3 - pip install boto3
- Configure AWS run aws configure
- Program accepts two parameters: website name and region
- Example: python aws_s3.py applesarereallycool us-west-2
- If successful, the return will be: "Website is live at: http://applesarereallycool.s3-website-us-west-2.amazonaws.com"
- Visiting the URL will display this: "Awesome Web Services! It worked if you're seeing this!"

## Libraries Used

- Boto3

## Contributors

AWS S3 Website Creator was originally created by Kevin J Nguyen on 11/14/16. 

## License

`AWS S3 Website Creator` is released under an [MIT License][mitLink]. See `LICENSE` for details.

**Copyright &copy; 2016-present Kevin J Nguyen.**

*Please provide attribution, it is greatly appreciated.*

[mitLink]:http://opensource.org/licenses/MIT
