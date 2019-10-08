# coding:utf-8
# 早上批切
import datetime
import logging
from db import DB
from rabbitmq_send import RabbitmqSend


class TSK1000(RabbitmqSend):

    def morning_bat_cut(self):
        logging.info('早上批切开始')
        sql = "select * from TBL_DATE_SYS_STAT"
        data = DB().qry_db_table(sql)
        txn_status = data[0][0]
        stlm_date = data[0][1]
        last_stlm_date = data[0][2]
        curr_batch_num = data[0][3]
        last_batch_num = data[0][4]
        upd_date_time = data[0][5]
        logging.info('状态=%s,当前清算日期=%s,上一清算日期=%s,当前批次号=%s,上一批次号=%s,最后更新时间=%s'
                     % (txn_status, stlm_date, last_stlm_date, curr_batch_num, last_batch_num, upd_date_time))
        last_batch_num = curr_batch_num;
        upd_date_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

        cur_seq = str(int(curr_batch_num[8:]) + 1)
        if len(cur_seq) == 1:
            cur_seq = "0" + cur_seq
        curr_batch_num = curr_batch_num[0:8] + cur_seq
        logging.debug(curr_batch_num)
        sql = "update TBL_DATE_SYS_STAT set txn_status=\"%s\",curr_batch_num=\"%s\",last_batch_num=\"%s\",upd_date_time=\"%s\"" \
                                            % ('0', curr_batch_num, last_batch_num, upd_date_time)
        DB().opr_db_table(sql)
        logging.info('早上批切结束')

        self.send(msg="hello")


TSK1000().morning_bat_cut()
