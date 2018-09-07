import request from 'superagent'

// 设置接口默认前缀
const root = '/api/v1/be/'

// 获取数据类型
const dataType = data => {
  return ({}).toString.call(data).match(/\s([a-zA-Z]+)/)[1].toLowerCase()
}

// 过滤值为null的请求参数数据
const filterNull = o => {
  for (let key in o) {
    if (o[key] === null) delete o[key]
    if (dataType(o[key]) === 'string') {
      o[key] = o[key].trim()
      if (o[key].length === 0) delete o[key]
    } else if (dataType(o[key]) === 'object') {
      o[key] = filterNull(o[key])
    } else if (dataType(o[key]) === 'array') {
      o[key] = filterNull(o[key])
    }
  }
  return o
}

// 发送请求并得到响应
const ajaxAgent = (method, url, params, success, failure) => {
  // 处理断网
  if (!navigator.onLine) return

  // 开始组织接口请求方法
  let r = request(method, url).type('application/json').withCredentials()
  // 处理参数
  if (params) {
    params = filterNull(params)
    if (method === 'POST' || method === 'PUT') {
      if (dataType(params) === 'object') params = JSON.stringify(params)
      r = r.send(params)
    } else if (method === 'GET' || method === 'DELETE') {
      r = r.query(params)
    }
  }
  r.then(res => {
    // 成功执行
    if (res.body.status === 0) {
      if (success) success(res.body, res)
    } else {
      if (failure) {
        failure(res.body, res, 'STATUS_ERROR')
      } else {
        // eslint-disable-next-line no-console
        console.error('Api Status Error')
      }
    }
  }).catch(err => {
    // 失败执行
    let res = err.response
    if (failure) {
      failure(res.body, res, 'HTTP_ERROR')
    } else {
      if (res.status === 401) {
        window.location.href = process.env.BASE_URL + '#/login'
      } else {
        // eslint-disable-next-line no-console
        console.error(err.message)
      }
    }
  })
}

// 处理报错信息
const checkTypeErr = (tip, data) => {
  try {
    throw new Error(tip + dataType(data))
  } catch (e) {
    // eslint-disable-next-line no-console
    console.error(e)
    return false
  }
}

// 验证请求时，传递的参数
const checkParams = (method, url, params, success, failure) => {
  // 检查成功执行入参
  if (dataType(success) !== 'function') {
    checkTypeErr('成功的回调函数位置接受的是一个Function,但是却得到一个', success)
  }
  // 检查失败执行入参
  if (failure && dataType(failure) !== 'function') {
    checkTypeErr('失败的回调函数位置接受的是一个Function,但是却得到一个', failure)
  }
  // 检查请求参数入参
  if (dataType(params) === 'object' || params === null) {
    ajaxAgent(method, url, params, success, failure)
  } else {
    checkTypeErr('接受的是一个对象或者为空(即null),但是却得到一个', params)
  }
}

export default {
  get (name, params, success, failure) {
    checkParams('GET', root + name, params, success, failure)
  },
  post (name, params, success, failure) {
    checkParams('POST', root + name, params, success, failure)
  },
  put (name, params, success, failure) {
    checkParams('PUT', root + name, params, success, failure)
  },
  delete (name, params, success, failure) {
    checkParams('DELETE', root + name, params, success, failure)
  },
  root () {
    return root
  },
  filterNull
}
