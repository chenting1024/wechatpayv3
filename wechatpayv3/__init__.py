# -*- coding: utf-8 -*-

from .type import WeChatPayType


class WeChatPay():
    def __init__(self,
                 wechatpay_type,
                 mchid,
                 private_key,
                 cert_serial_no,
                 appid,
                 apiv3_key,
                 notify_url=None,
                 cert_dir=None,
                 logger=None):
        """
        :param wechatpay_type: 微信支付类型，示例值：WeChatPayType.MINIPROG
        :param mchid: 直连商户号，示例值：'1230000109'
        :param private_key: 商户证书私钥，示例值：'MIIEvwIBADANBgkqhkiG9w0BAQE...'
        :param cert_serial_no: 商户证书序列号，示例值：'444F4864EA9B34415...'
        :param appid: 应用ID，示例值：'wxd678efh567hg6787'
        :param apiv3_key: 商户APIv3密钥，示例值：'a12d3924fd499edac8a5efc...'
        :param notify_url: 通知地址，示例值：'https://www.weixin.qq.com/wxpay/pay.php'
        :param cert_dir: 平台证书存放目录，示例值：'/server/cert'
        :param logger: 日志记录器，示例值logging.getLoger('demo')
        """
        from .core import Core

        self._type = wechatpay_type
        self._mchid = mchid
        self._appid = appid
        self._notify_url = notify_url
        self._core = Core(mchid=self._mchid,
                          cert_serial_no=cert_serial_no,
                          private_key=private_key,
                          apiv3_key=apiv3_key,
                          cert_dir=cert_dir,
                          logger=logger)

    def sign(self, data):
        """计算签名值paySign，供JSAPI、APP、NATIVE调起支付时使用
        :param data: 需要签名的参数清单，示例值：['wx888','1414561699','5K8264ILTKCH16CQ2502S....','prepay_id=wx201410272009395522657....']
        """
        sign_str = '\n'.join(data) + '\n'
        return self._core.sign(sign_str)

    def decrypt_callback(self, headers, body):
        """解密回调接口收到的信息
        :param headers: 回调接口收到的headers
        :param body: 回调接口收到的body
        """
        return self._core.decrypt_callback(headers, body)

    def decrypt(self, ciphtext):
        """解密微信支付平台返回的信息中的敏感字段
        :param ciphtext: 加密后的敏感字段，示例值：'Qe41VhP/sGdNeTHMQGlxCWiUyHu6XNO9GCYln2Luv4HhwJzZBfcL12sB+PgZcS5NhePBog30NgJ1xRaK+gbGDKwpg=='
        """
        return self._core.decrypt(ciphtext)

    from .businesscircle import points_notify, user_authorization
    from .complaint import (complant_complete, complant_detail_query,
                            complant_history_query, complant_image_download,
                            complant_image_upload, complant_list_query,
                            complant_notification_create,
                            complant_notification_delete,
                            complant_notification_query,
                            complant_notification_update, complant_response)
    from .marketing import (marketing_card_send, marketing_image_upload,
                            marketing_partnership_build,
                            marketing_partnership_query,
                            marketing_paygift_activity_create,
                            marketing_paygift_activity_detail,
                            marketing_paygift_activity_list,
                            marketing_paygift_activity_terminate,
                            marketing_paygift_goods_list,
                            marketing_paygift_merchant_add,
                            marketing_paygift_merchant_delete,
                            marketing_paygift_merchants_list)
    from .media import image_upload, video_upload
    from .parking import (parking_enter, parking_order, parking_order_query,
                          parking_service_find)
    from .payscore import (payscore_cancel, payscore_complete, payscore_create,
                           payscore_direct_complete, payscore_merchant_bill,
                           payscore_modify, payscore_pay, payscore_permission,
                           payscore_permission_query,
                           payscore_permission_terminate, payscore_query,
                           payscore_refund, payscore_refund_query,
                           payscore_sync)
    from .profitsharing import (profitsharing_add_receiver,
                                profitsharing_amount_query, profitsharing_bill,
                                profitsharing_delete_receiver,
                                profitsharing_order, profitsharing_order_query,
                                profitsharing_return,
                                profitsharing_return_query,
                                profitsharing_unfreeze)
    from .smartguide import (guides_assign, guides_query, guides_register,
                             guides_update)
    from .transaction import (close, combine_close, combine_pay, combine_query,
                              download_bill, fundflow_bill, pay, query,
                              query_refund, refund, trade_bill)
