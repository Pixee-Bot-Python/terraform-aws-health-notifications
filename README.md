# terraform-aws-health-notifications

This Terraform module creates a CloudWatch event rule and Lambda function to provide Slack notifications for AWS mainetnance notifications.

## Requirements

This module supports Terraform 0.12 and above.

## Usage

```
module "health_notifications" {
  source ="git::ssh://git@github.com/claranet/terraform-aws-health-notifications.git"

  slack_webhook = "https://hooks.slack.com/services/ABCDEFGHI/JKLMNOPQRST/UVWXYZ0123456789ABCDEFGH"
  account_name = "Playground"
  customer_name = "Claranet"
}
```

Note: If you require notifications from multiple regions, this module must be imported separately for each region individually.

# Inputs

| Name              | Description                                                                               | Type     | Default | Required |
|-------------------|-------------------------------------------------------------------------------------------|----------|---------|----------|
| **slack_webhook** | URL for the webhook to send Slack notifications to                                        | `string` |         | Yes      |
| **account_name**  | Friendly name for the AWS account to show in the notification                             | `string` |         | Yes      |
| **customer_name** | Friendly name for the customer the account is associated with to show in the notification | `string` |         | Yes      |

# Outputs

This module has no outputs.
