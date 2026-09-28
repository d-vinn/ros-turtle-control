#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "std_srvs/srv/empty.hpp"

class TurtleBridgeNode : public rclcpp::Node
{
public:
    TurtleBridgeNode() : Node("turtle_bridge_node")
    {
        // Python GUI로부터 /gui_command 토픽을 구독
        subscription_ = this->create_subscription<std_msgs::msg::String>(
            "/gui_command", 10,
            std::bind(&TurtleBridgeNode::command_callback, this, std::placeholders::_1));

        // Turtlesim 제어를 위한 퍼블리셔 및 서비스 클라이언트 생성
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
        reset_client_ = this->create_client<std_srvs::srv::Empty>("/reset");
    }

private:
    void command_callback(const std_msgs::msg::String::SharedPtr msg)
    {
        RCLCPP_INFO(this->get_logger(), "Received command from GUI: '%s'", msg->data.c_str());

        auto twist = geometry_msgs::msg::Twist();

        if (msg->data == "up") {
            twist.linear.x = 2.0;
            twist.angular.z = 0.0;
            publisher_->publish(twist);
        } 
        else if (msg->data == "down") {
            twist.linear.x = -2.0;
            twist.angular.z = 0.0;
            publisher_->publish(twist);
        } 
        else if (msg->data == "left") {
            twist.linear.x = 0.0;
            twist.angular.z = 2.0;
            publisher_->publish(twist);
        } 
        else if (msg->data == "right") {
            twist.linear.x = 0.0;
            twist.angular.z = -2.0;
            publisher_->publish(twist);
        } 
        else if (msg->data == "reset") {
            if (reset_client_->wait_for_service(std::chrono::seconds(1))) {
                auto request = std::make_shared<std_srvs::srv::Empty::Request>();
                reset_client_->async_send_request(request);
                RCLCPP_INFO(this->get_logger(), "Turtlesim Reset requested.");
            }
        }
    }

    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::Client<std_srvs::srv::Empty>::SharedPtr reset_client_;
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<TurtleBridgeNode>());
    rclcpp::shutdown();
    return 0;
}
