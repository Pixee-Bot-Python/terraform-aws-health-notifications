variable "account_name" {
  type = string
  description = "A friendly name for this account to include in the Slack notification"
}

variable "customer_name" {
  type = string
  description = "A friendly name for the customer to include in the Slack notification"
}

variable "slack_webhook" {
  type = string
  description = "A Slack Webhook URL to send notifications to"
}
