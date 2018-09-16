const rules = {
  name: [
    { required: true, message: '请输入名称', trigger: 'blur' },
    { max: 20, message: '名称长度过长', trigger: 'blur' }
  ],
  tag: [
    { required: true, message: '请输入关键词', trigger: 'blur' },
    { max: 20, message: '关键词长度过长', trigger: 'blur' }
  ],
  contact: [
    { max: 20, message: '联系人长度过长', trigger: 'blur' }
  ],
  mobile: [
    { pattern: /^1[34578]\d{9}$/, message: '手机号格式不正确', trigger: 'blur' }
  ],
  email: [
    { type: 'email', message: '电子邮箱格式不正确', trigger: 'blur' }
  ],
  website: [
    { type: 'url', message: '网址格式不正确', trigger: 'blur' }
  ],
  hits: [
    { type: 'number', message: '创作量只能为数字', trigger: 'blur' }
  ]
}

export default (str) => {
  let needRulesArr = str.split(',')
  let res = {}
  for (let i of needRulesArr) {
    res[i] = rules[i]
  }
  return res
}
