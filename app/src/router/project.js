import store from 'src/store'
const isAuthenticated = () => store.state.user.isLoggedIn

export default [
    {
      path: '/project/create',
      name: 'project-create',
      meta: { title: 'Project Create' },
      component: () => import(/* webpackChunkName: "project" */ 'src/views/project')
    }
]

