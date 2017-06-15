import datetime

from fabric.api import run, cd


def sim(instrument, days, popsize, strategy):
    with cd('zenbot'):
        params = dict(instrument=instrument, days=days, strategy=strategy, popsize=popsize,
                      timestamp=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M'))
        cmd = "cd zen && python -m scoop main.py {instrument} {days} {popsize} {strategy}".format(**params)
        total = '(nohup docker-compose exec -T server bash -c "{cmd}" > {instrument}_{strategy}_{days}_{popsize}_{timestamp}.out 2>&1 &) && sleep 1'.format(
            cmd=cmd, **params)
        print(total)
        run(total)


def remote(cmd,logfile):
    with cd('zenbot'):
        total = '(nohup docker-compose exec -T server bash -c "{cmd}" > {logfile} 2>&1 &) && sleep 1'.format(cmd=cmd,
                                                                                                         logfile=logfile)
        print(total)
        run(total)
