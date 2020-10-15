import meraki
API_KEY = "XXX"

#"complete the statement in line 4"
dashboard = meraki.DashboardAPI(API_KEY, suppress_logging=True)

#"complete the statement in line 8"
my_orgs = dashboard.organizations.getOrganizations()

#print(my_orgs)

for x in range(len(my_orgs)):
    print(my_orgs[x]['id']+' - '+my_orgs[x]['name'])
