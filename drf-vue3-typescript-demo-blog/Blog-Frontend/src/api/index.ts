import axios, {AxiosRequestConfig, AxiosResponse} from "axios";
import {ElMessage} from "element-plus";
import router from "../router";
import {getCookie} from "../utils";


const request = axios.create({
    baseURL: import.meta.env.MODE !== 'production' ? '/api' : '',
})

request.interceptors.request.use((config: AxiosRequestConfig) => {
    // Django SessionAuthentication need csrf token
    config.headers['X-CSRFToken'] = getCookie('csrftoken')
    return config
})


request.interceptors.response.use(
    (response: AxiosResponse) => {
        const data = response.data
        console.log('response => ', response)
        if (data.status === '401') {
            localStorage.removeItem('user');
            ElMessage({
                message: data.error,
                type: 'error',
                duration: 1.5 * 1000
            })
            return router.push('/login')
        } else if (data.status === 'error') {
            ElMessage({
                message: data.error || data.status,
                type: 'error',
                duration: 1.5 * 1000
            })
        }

        if (data.success === false && data.msg) {
            ElMessage({
                message: data.msg,
                type: 'error',
                duration: 1.5 * 1000
            })
        }

        return data
    },
    ({message, response}) => {
        console.log('err => ', message, response) // for debug
        if (response && response.data && response.data.detail) {
            ElMessage({
                message: response.data.detail,
                type: 'error',
                duration: 2 * 1000
            })
        } else {
            ElMessage({
                message: message,
                type: 'error',
                duration: 2 * 1000
            })
        }
        if (response && (response.status === 403 || response.status === 401)) {
            localStorage.removeItem('user');
            return router.push('/login')
        }
        return Promise.reject(message)
    }
)
export default request;