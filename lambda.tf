module "lambda" {
  source = "github.com/claranet/terraform-aws-lambda"

  function_name = "aws-health-notification-handler"
  description   = "Handles AWS Health notifications"
  handler       = "main.lambda_handler"
  runtime       = "python3.6"
  timeout       = 300

  // Specify a file or directory for the source code.
  source_path = "${path.module}/lambda/slack-notify/"

  // Add environment variables.
  environment = {
    variables = {
      SLACK_WEBHOOK = var.slack_webhook,
      ACCOUNT_NAME = var.account_name,
      ACCOUNT_NUMBER = data.aws_caller_identity.current.account_id,
      CUSTOMER_NAME = var.customer_name,
    }
  }
}
