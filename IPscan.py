import argparse
from urllib.request import urlopen , Request

def banner():
	#Banner creation
	print( """
        
  #####  #       ####### #     # ######  ####### ######  ####### #     # #######    ### ######      #####                                            
 #     # #       #     # #     # #     # #       #     # #     # ##    #    #        #  #     #    #     #  ####    ##   #    # #    # ###### #####  
 #       #       #     # #     # #     # #       #     # #     # # #   #    #        #  #     #    #       #    #  #  #  ##   # ##   # #      #    # 
 #       #       #     # #     # #     # #####   ######  #     # #  #  #    #        #  ######      #####  #      #    # # #  # # #  # #####  #    # 
 #       #       #     # #     # #     # #       #   #   #     # #   # #    #        #  #                # #      ###### #  # # #  # # #      #####  
 #     # #       #     # #     # #     # #       #    #  #     # #    ##    #        #  #          #     # #    # #    # #   ## #   ## #      #   #  
  #####  ####### #######  #####  ######  #       #     # ####### #     #    #       ### #           #####   ####  #    # #    # #    # ###### #    # 
                                                                                                                                                        
                                                                                                OPEN-SOURCE PROJECT | https://github.com/Amrita2000 
                                                                                                BY AMRITA NAYAK                                                                                                                                                                                                            
                                                                                                                                                                                                              """)

	helpmenu()
def helpmenu():
	parser = argparse.ArgumentParser()
	parser.add_argument('-o', dest='output' ,help='Specify Your output file name')
	parser.add_argument('-w', dest='IPWORDLIST' ,help='Specify Your IP Wordlists')
	args = parser.parse_args()
	with open(args.IPWORDLIST) as file:
		  wd=file.readlines()
	with open(args.output, 'w') as output_file:
		output_file.write("%s" %automation(wd))
		
	

def ipscan():
	req=Request("https://www.cloudflare.com/ips-v4",headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req)
	html = webpage.read().decode("utf-8")
	iplist=[]
	for i in html.split("\n"):
		iplist.append(i.split("/")[0])
	return(iplist)

	


def automation(wd):
	cloudip = ipscan()
	listip=[]
	print("CHECK YOUR OUTPUT FILE.........!!!!!")
	for i in wd:
		m=i.split("\n")[0]
		if m in cloudip:
			continue
		else:
			listip.append(m)
	return(listip)

				

				

if __name__ == "__main__":
	banner()
