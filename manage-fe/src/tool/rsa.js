// 引入 jsencrypt 库
import JSEncrypt from 'jsencrypt'
// 引入 RSA 加密公钥
import publicKey from '@/config/rsa_key.js'

// 导出加密函数
export default str => {
  let encrypt = new JSEncrypt()
  encrypt.setPublicKey(publicKey)
  return encrypt.encrypt(str)
}
