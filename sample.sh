export PATH=/home/ubuntu/djenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games


source /home/ubuntu/.bashrc
source /home/ubuntu/djenv/bin/activate

#export LANG=en_US.UTF-8
export LANG=zh_CN.GB18030

cd /home/ubuntu/djenv/airquality/

python /home/ubuntu/djenv/airquality/SampleJob.py
