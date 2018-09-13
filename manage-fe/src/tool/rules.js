const rules = {
  name: [
    { required: true, message: '请输入作者姓名', trigger: 'blur' },
    { max: 20, message: '作者姓名长度过长', trigger: 'blur' }
  ],
  mobile: [
    { pattern: /^1[34578]\d{9}$/, message: '请输入作者手机号', trigger: 'blur' }
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
