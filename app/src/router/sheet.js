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
        props: true,
        meta: { title: 'sheet Create' },
        component: () => import(/* webpackChunkName: "sheet-create" */ '@/views/sheetCreate')
    },
    {
        path: '/sheet/:sheetId',
        name: 'sheet-view',
        props: true,
        meta: { title: 'sheet' },
        component: () => import(/* webpackChunkName: "sheet-view" */ '@/views/sheetView')
    }
]

