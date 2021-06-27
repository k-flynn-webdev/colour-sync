import store from '@/store'
const isAuthenticated = () => store.state.user.isLoggedIn

export default [
    {
        path: '/project',
        name: 'project-list',
        meta: { title: 'Projects' },
        component: () => import(/* webpackChunkName: "project-list" */ '@/views/projectList')
    },
    {
        path: '/project/create',
        name: 'project-create',
        meta: { title: 'Project Create' },
        component: () => import(/* webpackChunkName: "project-create" */ '@/views/projectCreate')
    },
    {
        path: '/project/:projectId',
        name: 'project-view',
        props: true,
        meta: { title: 'Project' },
        component: () => import(/* webpackChunkName: "project-view" */ '@/views/projectView')
    }
]

