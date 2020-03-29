<template>
	<div>
		<div class="top">
  			<div><img @click="tohead" src="../assets/logo2.png"/></div>
  				<div class="titles">
  					<span class="title" @click="totend">趋势指数</span>
  					<span class="title" @click="toexperience">股票体检</span>
  					<span class="title" @click="toknowledge">知识分享</span>
  					<span class="title" @click="tous">关于我们</span>
  					<span class="title_i">咨询</span>
  				</div>
  		</div>
  		<div class="middle">
  			<div class="title">
  				<span>欢迎咨询</span>
  			</div>
  			<div class="info">
  				<div class="s_title">姓名*</div>
				<div class="input">
					<div class="fname_input">
  						<el-input class="fname" v-model="info.fname" />
						<div class="n_title">First Name</div>
				    </div>
					<div class="fname_input">
  						<el-input class="fname" v-model="info.fname" />
						<div class="n_title">Last Name</div>
				    </div>
				</div>
				<div class="s_title">电话*</div>
				<div class="p_input">
					<el-input class="phone" v-model="info.phone" />
				</div>
  			</div>
			<div class="submit">
				<div class="button" @click="submit">Submit</div>
			</div>
  		</div>
	</div>
</template>
<script>
	export default{
		name:'consult',
		data(){
			return{
				info:{
					fname:'',
					lname:'',
					phone:''
				}
			}
		},
		methods:{
			tohead(){
				this.$router.push('/')
			},
			tous(){
				this.$router.push('/us')
			},
      		toexperience(){
        		this.$router.push('/experience')
      		},
      		totend(){
      			this.$router.push('/tend')
      		},
      		handleSelect(key, keyPath){
        		console.log(key,keyPath)
      		},
      		toknowledge(){
      			this.$router.push('/knowledge')
			},
			submit(){
				this.$message.success('提交成功')
			}  
		}
	}
</script>
<style scoped lang="stylus">
.middle
	margin-top 160px
	.title
		text-align center
		color #c79288
		font-size 40px
	.info
		width 40%
		margin 30px 30%
		.input
			display flex
			justify-content space-between
			.fname_input
				width 48%
				.fname
					margin-bottom 10px
					width 100%
				.n_title
					font-size 12px
		.s_title
			margin 20px 0 10px 0
	.submit
		margin-top 40px
		display flex
		justify-content center
		.button
			padding 15px 30px
			color #c79288
			font-size 20px
			border 1px solid #c79288
			cursor pointer
			border-radius 5px
.top
	margin-top 50px
	width 100%
	display flex
	justify-content space-between
	align-items center
	img
		height 40px
		width  160px
		margin-left 140px
		cursor pointer
	.titles
		margin-right 100px
		color #484848
		.title_i
			margin-right 20px
			cursor pointer
			padding-bottom 5px
			border-bottom 1px solid #484848
		.title 
			margin-right 20px
			cursor pointer
			padding-bottom 5px
		.title:hover
			border-bottom 1px solid #484848
</style>