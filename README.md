# terraform-aws-health-notifications

This Terraform module creates a CloudWatch event rule and Lambda function to provide Slack notifications for AWS mainetnance notifications.

## Requirements

This module supports Terraform 0.12 and above.

## Usage

```
module "health_notifications" {
  source ="../"

  slack_webhook = "https://hooks.slack.com/services/ABCDEFGHI/JKLMNOPQRST/UVWXYZ0123456789ABCDEFGH"
  account_name = "Playground"
  customer_name = "Claranet"
}
```

Note: If you require notifications from multiple regions, this module must be imported separately for each region individually.
