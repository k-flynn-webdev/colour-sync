import { get } from 'lodash-es'

export const genericErrMixin = {
    methods: {
        handleError (err) {
            const message = get(err, 'response.data', err.message)

            this.$message.add({
                message: message.detail ? message.detail : message,
                class: 'is-error',
            })
            throw err
        }
    }
}

// todo : Currently broken
// todo : Tests
export const genericErrPlugin = {
    install(Vue, options) {
        Vue.$handleErr = (err) => {
            const message = get(err, 'response.data', err.message)

            this.$message.add({
                message: message.detail ? message.detail : message,
                class: 'is-error',
            })
            throw err
        }
    }
}


