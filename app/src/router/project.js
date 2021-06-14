import store from '@/store'
const isAuthenticated = () => store.state.user.isLoggedIn

export default [
    {
      path: '/project',
      name: 'project',
      children: [
        {
          path: 'create',
          name: 'project-create',
          meta: { title: 'Project Create' },
          component: () => import(/* webpackChunkName: "project" */ '../views/project')
        },
        // {
        //   path: 'profile',
        //   name: 'user-profile',
        //   meta: { title: 'Profile' },
        //   beforeEnter(to, from, next) {
        //     if (!isAuthenticated()) {
        //       next({ name: 'home' })
        //     }
        //     next()
        //   },
        //   component: () => import(/* webpackChunkName: "profile" */ '../views/user/profile')
        // },
      ]
    }
]

