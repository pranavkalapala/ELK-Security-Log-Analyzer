Security Log Analyzer (ELK Stack)

Project Overview

This repository documents the creation of a Security Information and Event Management (SIEM) pipeline using the ElK stack to ingest, parse, and analyze macOS system logs. The project's main objective was to transform raw, unstructured log data from a 5-minute time-boxed snapshot into actionable security intelligence. The implementation successfully established a system baseline and produced dashboards capable of detecting immediate anomalies, access failures, and program execution events on the mac host.

Project Relevance

The project is significantly relevant to the cybersecurity and forensics fields because it addresses the critical challenge of processing massive volumes of noisy, unstructured log data for effective threat detection and incident response. By demonstrating proficiency in applying custom Grok filtering, my project showcases the vital skill needed to establish host baselines and quickly prioritize critical alerts like access failures and execution anomalies. This capability is essential for any security practitioner needing to differentiate between normal system operations and suspicious activity.

Methodology

My project utilized Logstash as the data Processor, Elasticsearch as the scalable store, and Kibana as the Visualization Layer. I first had to download the ELK stack onto the kali vm. Originally I planned on using Filebeat to send my logs from my mac to the kali vm, but I was having problems with it so I decided to run "sudo log show --style syslog --last 7d ~/mac_logs_last_5m.txt" on the mac terminal. 7 days worth of logs ended up being around 2 million logs, so I kept lowering the time frame until I decided to go with 5 minutes. I emailed the txt file and downloaded it in kali, where I then coverted it to a json file using a python script called convert_to_json.py. I then created "mac_logs_5m.conf", a logstash file that would filter the txt file because the way the original mac logs were structured was incompatible with Kibana. I used grok parsing to break the single string into separate usable fields, the date filter to take that extracted timestamp_str and turn it into the required Kibana field, @timestamp, and I converted the pid field to an integer and renamed the original log line to raw_log_line for forensics. Then, I sent the edited data to Elasticsearch where it was indexed and stored, making it instantly searchable by Kibana. I then used Kibana to build my 4 dashboards,
