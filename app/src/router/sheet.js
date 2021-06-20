import store from '@/store'
const isAuthenticated = () => store.state.user.isLoggedIn

export default [
    {
        path: '/sheet',
        name: 'sheet-list',
        meta: { title: 'sheets' },
        component: () => import(/* webpackChunkName: "sheet-list" */ '@/views/sheetList')
    },
    {
        path: '/project/:projectId/sheet/create',
        name: 'sheet-create',
        meta: { title: 'sheet Create' },
        props: {
            type: 'projectId'
        },
        component: () => import(/* webpackChunkName: "sheet-create" */ '@/views/sheetCreate')
    },
    {
        path: '/sheet/:sheet',
        name: 'sheet-view',
        meta: { title: 'sheet' },
        component: () => import(/* webpackChunkName: "sheet-view" */ '@/views/sheetView')
    }
]

