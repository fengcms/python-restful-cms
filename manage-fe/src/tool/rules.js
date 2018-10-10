const rules = type => {
  return {
    name: [
      { required: true, message: `请输入${type}名称`, trigger: 'blur' },
      { max: 20, message: `${type}名称长度过长`, trigger: 'blur' }
    ],
    account: [
      { required: true, message: `请输入${type}账号`, trigger: 'blur' },
      { max: 20, message: `${type}账号长度过长`, trigger: 'blur' }
    ],
    tag: [
      { required: true, message: `请输入关键词`, trigger: 'blur' },
      { max: 20, message: `关键词长度过长`, trigger: 'blur' }
    ],
    contact: [
      { max: 20, message: `联系人长度过长`, trigger: 'blur' }
    ],
    mobile: [
      { pattern: /^1[34578]\d{9}$/, message: `手机号格式不正确`, trigger: 'blur' }
    ],
    email: [
      { type: 'email', message: `电子邮箱格式不正确`, trigger: 'blur' }
    ],
    website: [
      { type: 'url', message: `网址格式不正确`, trigger: 'blur' }
    ],
    hits: [
      { type: 'number', message: `创作量只能为数字`, trigger: 'blur' }
    ],
    password: [
      { required: true, message: `请输入登录密码`, trigger: 'blur' },
      { max: 16, min: 6, message: `密码长度为6-16之间`, trigger: 'blur' },
      { pattern: /^[a-zA-Z0-9_]+$/, message: `密码只允许数字大小写字母以及下划线组成`, trigger: 'blur' }
    ],
    old_password: [
      { required: true, message: `请输入原登录密码`, trigger: 'blur' },
      { max: 16, min: 6, message: `密码长度为6-16之间`, trigger: 'blur' },
      { pattern: /^[a-zA-Z0-9_]+$/, message: `密码只允许数字大小写字母以及下划线组成`, trigger: 'blur' }
    ],
    new_password: [
      { required: true, message: `请输入新登录密码`, trigger: 'blur' },
      { max: 16, min: 6, message: `密码长度为6-16之间`, trigger: 'blur' },
      { pattern: /^[a-zA-Z0-9_]+$/, message: `密码只允许数字大小写字母以及下划线组成`, trigger: 'blur' }
    ]
  }
}

export default (str, type) => {
  let needRulesArr = str.split(',')
  let res = {}
  for (let i of needRulesArr) {
    res[i] = rules(type)[i]
  }
  return res
}
