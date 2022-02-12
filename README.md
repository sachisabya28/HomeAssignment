## Adjust
```bash
Assignment : https://gist.github.com/kotik-adjust/4883e33c439db6de582fd0986939045c
```
###### Setup the app ######
## Only run below step if initial setup is done, else start app the directly using below command.
```bash
sh run.sh
```

```bash
git clone https://github.com/sachisabya28/HomeAssignment.git
cd adjust
sh setup.sh
sh run.sh
```

###### Unitest ######

```bash
cd ~/adjustapi/test
python test_api.py
```

1. Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.

```bash
http://127.0.0.1:8000/api/?date__lte=2017-06-01&group_by=country&group_by=channel&ordering=-clicks&limit=impressions&limit=clicks
```

2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.

```bash
http://127.0.0.1:8000/api/?date__range=2017-05-01,2017-05-31&ordering=date&os=ios&group_by=date&limit=installs
```

3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.

```bash
http://127.0.0.1:8000/api/?date__lte=2017-06-01&country=US&group_by=os&ordering=-revenue&limit=revenue
```

4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.

```bash
http://127.0.0.1:8000/api/?country=CA&group_by=channel&cpi=cpi&limit=spend&ordering=-cpi
```


