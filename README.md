# Computer's Automated WatchDog
Automated Computer Health Check's WatchDog 


The script will check every minute with 1 second sleep: - CPU usage
                                                        - Disk space
                                                        - Available memory
                                    
If CPU usage is greater than 80% or Disk Space is less than 20% or Available Memory is less than 500MB: The on-site sys-admin will be notified with screen pop-up notification and an alerting email will be automatically sent to the off-site sys-admin.
