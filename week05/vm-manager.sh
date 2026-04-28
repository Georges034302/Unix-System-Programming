#!/usr/bin/env bash

get_id() {
  aws ec2 describe-instances \
    | grep '"InstanceId"' \
    | head -1 \
    | sed 's/[",]//g' \
    | awk '{print $2}'
}

get_ip() {
  ID=$(get_id)

  aws ec2 describe-instances --instance-ids "$ID" \
    | grep '"PublicIpAddress"' \
    | head -1 \
    | sed 's/[",]//g' \
    | awk '{print $2}'
}

get_status() {
  ID=$(get_id)

  aws ec2 describe-instances --instance-ids "$ID" \
    | grep '"Name"' \
    | head -1 \
    | sed 's/[",]//g' \
    | awk '{print $2}'
}

start_instance() {
  ID=$(get_id)
  echo "Starting instance: $ID"
  aws ec2 start-instances --instance-ids "$ID"
}

stop_instance() {
  ID=$(get_id)
  echo "Stopping instance: $ID"
  aws ec2 stop-instances --instance-ids "$ID"
}

open_web() {
  IP=$(get_ip)
  echo "Opening http://$IP"
  google-chrome "http://$IP" 2>/dev/null
}

PS3="Choose option: "

select option in i s e p w v q
do
  case $option in
    i) get_id ;;
    s) start_instance ;;
    e) stop_instance ;;
    p) get_ip ;;
    w) open_web ;;
    v) get_status ;;
    q) break ;;
    *) echo "Invalid option" ;;
  esac
done
