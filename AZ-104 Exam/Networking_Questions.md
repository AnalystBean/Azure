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

## QUESTION 3

How do resources on Azure use a virtual network?


All resources must be connected to a virtual network to use the Azure platform.


> ***Azure Virtual Network enables Azure resources to securely communicate with each other, the internet, and on-premises networks.***


Resources on a free account don't have to be on a virtual network to use Azure.


All Azure resources that communicate with the public internet must be on a virtual network.




**Azure Virtual Network enables Azure resources to securely communicate with each other, the internet, and on-premises networks. Key scenarios that you can accomplish a virtual network include: communication of Azure resources with the internet, communication between Azure resources, communication with on-premises resources, filtering network traffic, routing network traffic, and integration with Azure services. Reference: Why use an Azure Virtual network?**

## QUESTION 4

In which scenario/s would you use an Application Gateway?




> ***To host multiple websites***


> ***For incoming traffic, to make routing decisions based on additional attributes of an HTTP request, such as URI path or host headers***


To manage the IP addresses for an Azure subscription and ensure only secure traffic is allowed


To send encrypted traffic between an Azure Virtual Network and an on-premises location over the public internet


To make sure the connection from a virtual network to the internet is secure


**You can use multi-site hosting to use the same Application Gateway for more than one website. You can, in fact, add up to 100 websites to the same instance of an Application Gateway. This will both save you on cost and complexity.

An Application Gateway is similar to a load balancer, but it can redirect traffic based on attributes in the HTTP request, the request coming in from the internet. You can have a VM handling video, one handling images and so on. Application Gateways do not handle traffic security, nor manage any virtual networks.**

## QUESTION 5

What is an address space on a virtual network?


> ***A range of IP addresses that can be assigned to resources attached to the virtual network***


A portion of the complete address space for a given Azure subscription that can be assigned to a virtual network


A reserved number of public IP addresses that you can use to connect a virtual network to the public internet


A definition of what types of resources can connect to either a private or public network hosted on Azure


**An address space on a virtual network is a number of IP addresses that are unique only on the specific virtual network. These IP addresses are assigned to resources connected to the VNet, which allows the resources to interact and communicate. There is no limit to the number of VNets you can have, nor on the number of address spaces.**

## QUESTION 6

What is the best scenario for using Azure ExpressRoute?


> ***Connecting your on-premises networks into the Microsoft cloud over a private connection with the help of a connectivity provider***


Connecting your on-premises networks into the Microsoft cloud over the public internet with the help of a connectivity provider


Connecting your on-premises networks into the Microsoft cloud over a private connection without a connectivity provider


Extending a VLAN to Azure using ExpressRoute

**ExpressRoute lets you extend your on-premises networks into the Microsoft cloud over a private connection with the help of a connectivity provider. With ExpressRoute, you can establish connections to Microsoft cloud services, such as Microsoft Azure and Microsoft 365.**


