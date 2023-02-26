## QUESTION 1

Why would you use a content delivery network?



To ensure maximum uptime for an application that is hosted in more than one datacenter


For incoming traffic, to make routing decisions based on additional attributes of an HTTP request, such as URI path or host headers


> ***To better handle instantaneous high loads, such as the start of a product launch event***


To ensure requests made from users are securely handled and served


> ***To provide better performance and improved user experience for end users***


**A CDN keeps a recent copy of your web application and can deliver this much faster to users close to an endpoint. CDNs can handle a lot more data than a typical web server, which makes it ideal to handle traffic spikes as well. CDNs don't generally handle individual traffic routing rules, nor security.**
## QUESTION 2

Which benefits does adding a load balancer provide?



A load balancer ensures the load is evenly distributed between two to five virtual machines only.


> ***A load balancer ensures only healthy servers process requests.***


> ***When there is too much incoming network traffic for a single VM to handle, a load balancer can distribute the load to many VMs.***


> ***A load balancer can log traffic that passes through it.***


When a virtual disk is running low on space on a virtual machine (but not low enough to cause the VM to be unhealthy), the incoming data can be preemptively redirected to another virtual machine to manage the load.


**A load balancer sits in front of two or more virtual machines to manage, and balance, the load to the virtual machines. This can be based on amount of incoming traffic or specific properties in the traffic. A load balancer has nothing to do with virtual disks, and the max number of VMs to manage goes up to 1,000. A load balancer ensures only healthy instances receive traffic and will stop sending traffic to any server that does not pass health checks. All Azure load balancers can log traffic that passes through them.**