import store from '@/store'
const isAuthenticated = () => store.state.user.isLoggedIn

export default [
    {
      path: '/user',
      name: 'user',
      children: [
        {
          path: 'register',
          name: 'user-register',
          meta: { title: 'Register' },
          component: () => import(/* webpackChunkName: "loginOrRegister" */ '../views/user/loginOrRegister')
        },
        {
          path: 'login',
          name: 'user-login',
          meta: { title: 'Login' },
          component: () => import(/* webpackChunkName: "loginOrRegister" */ '../views/user/loginOrRegister')
        },
        {
          path: 'verify',
          name: 'user-verify-email',
          meta: { title: 'Verify' },
          component: () => import(/* webpackChunkName: "verifyEmail" */ '../views/user/verifyEmail')
        },
        {
          path: 'reset',
          name: 'user-reset-password',
          meta: { title: 'Reset' },
          component: () => import(/* webpackChunkName: "resetPassword" */ '../views/user/resetPassword')
        },
        {
          path: 'profile',
          name: 'user-profile',
          meta: { title: 'Profile' },
          beforeEnter(to, from, next) {
            if (!isAuthenticated()) {
              next({ name: 'home' })
            }
            next()
          },
          component: () => import(/* webpackChunkName: "profile" */ '../views/user/profile')
        },
      ]
    }
]

