<%@ page language="java" import="java.sql.*" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
        <title>Insert title here</title>
    </head>
    <body>
    <%
        String name=request.getParameter("username");
        String pass=request.getParameter("password");
        
        	String drivername="com.microsoft.jdbc.sqlserver.SQLServerDriver";	
	String uname="sqlinjection";	
	String userpassword="sql";	
	String dbname="pysqlinject";	
	String url = "jdbc:microsoft:sqlserver://127.0.0.1:1433;DatabaseName="+dbname;
	Class.forName(drivername).newInstance();
	Connection con=DriverManager.getConnection(url,uname, userpassword);	


        Statement st = con.createStatement();
        ResultSet res = st.executeQuery("select * from userinfo where name1 = '"+ name +"' and passwd = '"+ pass + "'");
        if(res.next()){
            out.print("<p>用户名:" + res.getString(1) + " 密码 " +res.getString(2) + "</p></br>");
            out.print("登陆成功");
        }
        else
            out.print("用户名或密码错误" + name);
    %>
    </body>
</html>

