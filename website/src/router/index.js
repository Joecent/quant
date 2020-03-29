import Vue from 'vue'
import Router from 'vue-router'
import lazy from '@/utils/sdk/lazy'

Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'index',
      component: lazy('index')
    },
    {
      path: '/experience',
      name: 'experience',
      component: lazy('experience')
    },
    {
    	path:'/knowledge',
    	name:'knowledge',
    	component: lazy('knowledge')
    },
    {
      path: '/tend',
      name: 'tend',
      component: lazy('tend')
    },
    {
      path: '/us',
      name: 'us',
      component: lazy('us')
    },
    {
      path: '/consult',
      name: 'consult',
      component: lazy('consult')
    },
    {
    	path:'/article',
    	name:'article',
    	component: lazy('article')
    }
  ]
})
