# Computer's Automated WatchDog
Automated Computer Health Check's WatchDog 


The script will check every minute with 1 second sleep: - CPU usage
                                                        - Disk space
                                                        - Available memory
                                    
If CPU usage is greater than 80% or Disk Space is less than 20% or Available Memory is less than 500MB: The on-site sys-admin will be notified with screen pop-up notification and an alerting email will be automatically sent to the off-site sys-admin.


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Starting from 15 October 2020, I am working on transforming this code into useful software to use by implementing nice looking GUI. I am also implementing new features such as bandwith test, latency test, ping test and automated pdf report sent automatically by email. Here's an overview.


![system watchdog.gif](https://github.com/IT-Support-L2/Computer-s-Automated-WatchDog/blob/master/system%20watchdog.gif)




