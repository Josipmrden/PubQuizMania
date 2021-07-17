import LabelingSection from './components/LabelingSection';
import QuizSection from './components/QuizSection';
import PVPSection from './components/PVPSection';
import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
        { path: '/', match: 'exact', component: QuizSection}, 
        { path: '/labeling', component: LabelingSection },
        { path: '/quiz', component: QuizSection },
        { path: '/pvp', component: PVPSection }
    ]

export const router = new VueRouter({
    mode: 'history',
    routes
})