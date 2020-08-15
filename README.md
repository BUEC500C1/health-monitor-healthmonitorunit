# health-monitor-healthmonitorunit
health-monitor-healthmonitorunit created by GitHub Classroom

## Team Members
- Sensor module: Chenhui Zhu (zhuch@bu.edu)
- Database module: Junyou Chi (chi12@bu.edu)
- Alert module: Ganghao Li (lighao@bu.edu)
- Monitor module: Fengxu Tu (fengxutu@bu.edu)
- Prediction (AI) module：Jialun Wang (wjl1996@bu.edu)
- Processor Integration: Hanchen Zhang (hczhang@bu.edu)

## User story
- As a nurse in a hospital, I want to see my patient’s pulse, blood pressure, and blood oxygen concentration on configurable time intervals.
- I also want to get alerts and warning if any of the data go out of the threshold value.
- I want to get future predictions of all those data based on an AI module.

### Integration:
```
git clone https://github.com/BUEC500C1/health-monitor-healthmonitorunit/tree/Hanchen-Zhang
```
and then 
```
python processor.py
```
And you can see the following example result: <br/>
- Green Message: None of the data out of threshold <br/>
- Red box: Some data elements out of the threshold value and refered to related medical description <br/>
- Yellow box: current elements are normal but could runs out of the threshold in the future <br/><br/><br/>
