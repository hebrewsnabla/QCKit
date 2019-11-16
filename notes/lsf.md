## quota
limitations of disk of a user
```bash
[wli@c01n01 program]$ mmlsquota
                         Block Limits                         |     File Limits
Filesystem type      KB      quota      limit  in_doubt grace | files   quota   limit in_doubt  grace 
ess        USR   1049675264 1048576000 1153433600  0  expired | 958454 9000000 10000000    0     none

                         Block Limits                         |     File Limits
Filesystem type      KB      quota    limit   in_doubt  grace | files quota  limit in_doubt  grace  
ssd        USR     983552 1048576000 2097152000   0     none  |   25 9000000 10000000   0    none

```
* `quota`: soft limit. Disk write will be banned after grace expired
* `limit`: hard limit. Banned immediately
In nju cluster, grace for `/share/user`(ess) is 7 days, for `/scratch/user/`(ssd) is 15 days
