resource "aws_cloudwatch_event_rule" "health" {
  name = "capture_aws_maintenance_notifications"
  description = "Captures AWS maintenance notifications for forwarding to Slack"

  event_pattern = <<EOF
{
  "source": ["aws.health"],
  "detail-type": ["AWS Health Event"]
}
EOF
}

resource "aws_cloudwatch_event_target" "health_lambda" {
  rule      = aws_cloudwatch_event_rule.health.name
  target_id = "TriggerHealthNotificationLambda"
  arn       = module.lambda.function_arn
}
